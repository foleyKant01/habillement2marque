import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators, FormArray } from '@angular/forms';
import { Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-create-products',
  templateUrl: './create-products.component.html',
  styleUrls: ['./create-products.component.scss']
})
export class CreateProductsComponent implements OnInit {

  createproducts!: FormGroup;
  loading = false;
  success = false;
  files: File[] = [];
  successMessage: string = '';
  errorMessage: string = '';

  colors: string[] = [
    'Noir', 'Blanc', 'Gris', 'Marron', 'Beige',
    'Bleu marine', 'Rouge', 'Vert', 'Jaune',
    'Bleu', 'Rose', 'Violet', 'Orange', 'Multi'
  ];

  constructor(
    private fb: FormBuilder,
    private http: BackService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.createproducts = this.fb.group({
      name: [null, Validators.required],
      type: [null, Validators.required],
      model: [null],
      style: [null],
      talon_cm: [null],
      material: [null],
      description: [null, Validators.required],
      price: [null, Validators.required],
      price_received: [null, Validators.required],

      variants: this.fb.array([]),
    });

    // 👇 au moins une variante
    this.addVariant();
  }

  // =========================
  // 🔥 VARIANTS
  // =========================

  get variants(): FormArray {
    return this.createproducts.get('variants') as FormArray;
  }

  newVariant(): FormGroup {
    return this.fb.group({
      color: [null, Validators.required],
      pointures: this.fb.array([])
    });
  }

  addVariant(): void {
    const variant = this.newVariant();
    this.variants.push(variant);
    this.addPointure(this.variants.length - 1);
  }

  removeVariant(index: number): void {
    this.variants.removeAt(index);
  }

  // =========================
  // 🔥 POINTURES
  // =========================

  getPointures(index: number): FormArray {
    return this.variants.at(index).get('pointures') as FormArray;
  }

  newPointure(): FormGroup {
    return this.fb.group({
      size: [null, Validators.required],
      stock: [1, Validators.required]
    });
  }

  addPointure(index: number): void {
    this.getPointures(index).push(this.newPointure());
  }

  removePointure(i: number, j: number): void {
    this.getPointures(i).removeAt(j);
  }

  // =========================
  // 📁 IMAGES
  // =========================

  onFileChange(event: any): void {
    const selectedFiles = event.target.files;

    if (selectedFiles.length > 0) {
      this.files = [];

      for (let i = 0; i < selectedFiles.length; i++) {
        this.files.push(selectedFiles[i]);
      }
    }
  }

  // =========================
  // 🚀 SUBMIT
  // =========================

  Createproducts(): void {
    // if (this.createproducts.invalid) return;

    this.loading = true;

    const formData = new FormData();
    const formValue = this.createproducts.value;

    // 🔹 produit
    formData.append('type', formValue.type);
    formData.append('name', formValue.name);
    formData.append('model', formValue.model);
    formData.append('style', formValue.style);
    formData.append('description', formValue.description);
    formData.append('price', formValue.price);
    formData.append('price_received', formValue.price_received);
    formData.append('material', formValue.material);
    formData.append('talon_cm', formValue.talon_cm);

    // 🔥 IMPORTANT : variants
    formData.append('variants', JSON.stringify(formValue.variants));

    // 🔹 images
    this.files.forEach(file => {
      formData.append('image_file', file);
    });

    console.log('DATA SENT:', formValue);

    // variables à ajouter dans le component

// dans ton subscribe
this.http.CreateProducts(formData).subscribe({
  next: (response: any) => {
    this.loading = false;

    if (response.status === 'success') {
      this.successMessage = response.message || 'Produit créé avec succès !';
      this.errorMessage = '';

      // reset du form
      this.createproducts.reset();
      this.variants.clear();
      this.addVariant();
      this.files = [];

      // cacher le message après 3s
      setTimeout(() => this.successMessage = '', 3000);
    } else {
      // cas où API renvoie status != success
      this.errorMessage = response.message || 'Erreur lors de la création du produit';
      this.successMessage = '';

      setTimeout(() => this.errorMessage = '', 3000);
    }
  },

  error: (err) => {
    this.loading = false;

    this.errorMessage =
      err?.error?.message ||
      err?.error?.error ||
      'Erreur lors de la création du produit';

    this.successMessage = '';

    // cacher message après 3s
    setTimeout(() => this.errorMessage = '', 3000);

    console.error(err);
  }
});
  }
}