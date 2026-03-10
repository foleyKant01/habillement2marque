import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
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
  file: File | null = null;
  selectedType: string | null = null;

  // Couleurs et tailles dynamiques
  colors: string[] = ['Noir', 'Blanc', 'Gris', 'Marron', 'Beige', 'Bleu marine', 'Rouge', 'Vert', 'Jaune', 'Bleu', 'Rose', 'Violet', 'Orange', 'Multi'];
  taillesVe: string[] = ['XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL'];

  constructor(
    private fb: FormBuilder,
    private http: BackService,
    private router: Router
  ) { }

  ngOnInit(): void {
    // Création du formulaire
    this.createproducts = this.fb.group({
      name: [null, Validators.required],
      type: [null, Validators.required],
      model: [null],
      style: [null],
      details: [null],
      material: [null],
      talon_cm: [null],
      description: [null, Validators.required],
      price: [null, Validators.required],
      image_file: [null, Validators.required],
      inventory_level: [null, Validators.required],
      price_received: [null, Validators.required],
      color: [null, Validators.required],
    });

    // Suivi des changements du type pour gérer les champs dynamiques
    this.createproducts.get('type')?.valueChanges.subscribe(value => {
      // this.selectedType = value;
      if (value === 'Chaussures Homme' || value === 'Chaussures Femme') {
        this.createproducts.get('talon_cm')?.setValidators([Validators.required]);
      } else {
        this.createproducts.get('talon_cm')?.clearValidators();
      }
      this.createproducts.get('talon_cm')?.updateValueAndValidity();
    });
  }

  // Gestion du fichier
  onFileChange(event: any): void {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      this.file = selectedFile;
      this.createproducts.get('image_file')?.setValue(selectedFile);
    }
  }

  // Création du produit
  Createproducts(): void {
    if (this.createproducts.invalid || !this.file) {
      return; // Formulaire incomplet
    }

    this.loading = true;
    const formData = new FormData();
    formData.append('name', this.createproducts.get('name')?.value);
    formData.append('type', this.createproducts.get('type')?.value);
    formData.append('description', this.createproducts.get('description')?.value);
    formData.append('price', this.createproducts.get('price')?.value);
    formData.append('inventory_level', this.createproducts.get('inventory_level')?.value);
    formData.append('price_received', this.createproducts.get('price_received')?.value);
    formData.append('color', this.createproducts.get('color')?.value);
    formData.append('model', this.createproducts.get('model')?.value);
    formData.append('style', this.createproducts.get('style')?.value);
    formData.append('details', this.createproducts.get('details')?.value);
    formData.append('material', this.createproducts.get('material')?.value);
    formData.append('image_file', this.file as File);

    // Champs dynamiques
    if (this.createproducts.get('talon_cm')?.value) {
      formData.append('talon_cm', this.createproducts.get('talon_cm')?.value);
    }

    // Appel API
    this.http.CreateProducts(formData).subscribe({
      next: (response: any) => {
        this.loading = false;
        this.success = true;
        // Reset du formulaire
        this.createproducts.reset();
        this.file = null;
        setTimeout(() => this.success = false, 3000); // Message succès 3s
      },
      error: (err) => {
        console.error(err);
        this.loading = false;
        alert('Erreur lors de la création du produit');
      }
    });
  }

  // Propriétés pour *ngIf
  get showColor(): boolean {
    return !!this.selectedType && this.selectedType !== 'Jouer Enfant';
  }

  get showTailleVe(): boolean {
    return this.selectedType === 'Vêtement Homme' || this.selectedType === 'Vêtement Femme' || this.selectedType === 'Sous Vêtement Homme' || this.selectedType === 'Sous Vêtement Femme';
  }
}
