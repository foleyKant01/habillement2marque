import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { Router, RouterOutlet } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-create-products',
  templateUrl: './create-products.component.html',
  styleUrls: ['./create-products.component.scss']
})
export class CreateProductsComponent implements OnInit {

  loading= false;
  delayDuration= 2000
  success = false;
  file: any;



  ngOnInit(): void {
    // throw new Error('Method not implemented.');
  }

  constructor(private router: Router, private fb: FormBuilder, private http: BackService){}

  createproducts: FormGroup = new FormGroup(
    {
      name: new FormControl(null, Validators.required),
      type: new FormControl(null, Validators.required),
      description: new FormControl(null, Validators.required),
      price: new FormControl(null, Validators.required),
      image_file: new FormControl(null, Validators.required),
      inventory_level: new FormControl(null, Validators.required),
      price_received: new FormControl(null, Validators.required),
      weight: new FormControl(null, Validators.required),
      color: new FormControl(null, Validators.required),
      taille1: new FormControl(null, Validators.required),
      taille2: new FormControl(null, Validators.required),
      taille3: new FormControl(null, Validators.required),
      taille4: new FormControl(null, Validators.required),
      // taille5: new FormControl(null, Validators.required),
    }
  )

  onFileChange(event: any) {
    console.log(event);
    let file = event.target.files[0];
    this.file = file;
    console.log(this.file);

    return file;
  }

  Createproducts(){
    if (this.createproducts.valid) {
      this.loading = true;
      const formData: FormData = new FormData();
      formData.append('name', this.createproducts.get('name')?.value);
      formData.append('type', this.createproducts.get('type')?.value);
      formData.append('description', this.createproducts.get('description')?.value);
      formData.append('price', this.createproducts.get('price')?.value);
      formData.append('image_file', this.file as File);
      formData.append('inventory_level', this.createproducts.get('inventory_level')?.value);
      formData.append('price_received', this.createproducts.get('price_received')?.value);
      formData.append('weight', this.createproducts.get('weight')?.value);
      formData.append('color', this.createproducts.get('color')?.value);
      formData.append('taille1', this.createproducts.get('taille1')?.value);
      formData.append('taille2', this.createproducts.get('taille2')?.value);
      formData.append('taille3', this.createproducts.get('taille3')?.value);
      formData.append('taille4', this.createproducts.get('taille4')?.value);

    this.http.CreateProducts(formData).subscribe({
      next : (reponse:any)=>{
        console.log(reponse);
        setTimeout(() => {
          this.loading = false;
          this.success = true;
          window.location.reload();
        }, this.delayDuration);

      },
      error: (error) => {
        console.error(error);
        setTimeout(() => {
          this.loading = false;
        }, this.delayDuration); // Désactiver le spinner en cas d'erreur
      }
    })
    }
  }


}
