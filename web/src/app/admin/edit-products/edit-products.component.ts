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

  constructor(private router: ActivatedRoute, private http: BackService, private formBuilder: FormBuilder){
    this.updateProductsForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required]
    });
  }
  ngOnInit(): void {
// Récupérer l'ID de la catégorie depuis l'URL
this.productUid = this.router.snapshot.params['pr_uid'];

// Charger les informations de la catégorie à modifier
this.http.ReadSingleProducts(this.productUid).subscribe((product: any) => {
  // Pré-remplir le formulaire avec les informations de la catégorie
  this.updateProductsForm.patchValue({
    name: product.name,
    description: product.description
  });
});
}
//Gar de transport
//Des compagnies de transport pour des destination interne et externe du pays


  updateProducts() {
    if (this.updateProductsForm.valid) {
      this.loading = true;

      const updatedCategory = {
        ca_uid: this.productUid,
        name: this.updateProductsForm.value.name,
        description: this.updateProductsForm.value.description
      };

      // Appeler la fonction de mise à jour de la catégorie dans le service API
      this.http.UpdateProducts(updatedCategory).subscribe({
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

