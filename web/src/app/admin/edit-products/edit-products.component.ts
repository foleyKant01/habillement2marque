import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-edit-products',
  templateUrl: './edit-products.component.html',
  styleUrls: ['./edit-products.component.scss']
})
export class EditProductsComponent implements OnInit {
  updateProductsForm: FormGroup;
  loading = false;
  productUid: any;
  delayDuration= 2000
  success = false;
  product: any; // Stocke les détails du produit


  constructor(private route: ActivatedRoute, private http: BackService, private formBuilder: FormBuilder){
    this.updateProductsForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      price: ['', Validators.required],
      image: ['', Validators.required],
      taille1: ['', Validators.required],
      taille2: ['', Validators.required],
      taille3: ['', Validators.required],
      taille4: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
    });

    this.readSingleProducts();
    this.updateProducts();
  }

  readSingleProducts(): void {
    let body = {
      pr_uid: this.productUid
    }
    this.http.ReadSingleProducts(body).subscribe({
      next: (response: any) => {
        this.product = response?.user; // Stocker les produits dans le tableau
        // console.log(this.product)

      },
      error: (error) => {
        console.error('Failed to load products:', error);
      }
    });
      // }
    }

  updateProducts() {
    if (this.updateProductsForm.valid) {
      this.loading = true;

      const updateProducts = {
        pr_uid: this.productUid,
        name: this.updateProductsForm.value.name,
        description: this.updateProductsForm.value.description,
        price: this.updateProductsForm.value.price,
        image: this.updateProductsForm.value.image,
        taille1: this.updateProductsForm.value.taille1,
        taille2: this.updateProductsForm.value.taille2,
        taille3: this.updateProductsForm.value.taille3,
        taille4: this.updateProductsForm.value.taille4,
      };

      // Appeler la fonction de mise à jour de la catégorie dans le service API
      this.http.UpdateProducts(updateProducts).subscribe({
        next: (response: any) => {
          console.log(response);
          setTimeout(() => {
            this.loading = false;
            this.success = true;
            window.location.reload();
          }, this.delayDuration);
          // Rediriger ou afficher un message de succès
        },
        error: (error) => {
          console.error(error);
          setTimeout(() => {
            this.loading = false;
          }, this.delayDuration);
          // Afficher un message d'erreur
        }
      });
    }
  }

}
