import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-view-single-products',
  templateUrl: './view-single-products.component.html',
  styleUrls: ['./view-single-products.component.scss']
})
export class ViewSingleProductsComponent implements OnInit{

  product: any; // Stocke les détails du produit
  data: any;
  productUid: string | undefined;

  constructor(private route: ActivatedRoute, private http: BackService, private router: Router) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
      console.log(this.productUid)

    });

    this.readSingleProducts();
  }

  readSingleProducts(): void {
    let body = {
      pr_uid: this.productUid
    }
    this.http.ReadSingleProducts(body).subscribe({
      next: (response: any) => {
        this.product = response?.product; // Stocker les produits dans le tableau
        console.log(this.product)

      },
      error: (error) => {
        console.error('Failed to load products:', error);
      }
    });
      // }
    }

    deleteProduct(pr_uid: string) {
      if (confirm('Voulez-vous vraiment supprimer ce produit ?')) {
        this.http.DeleteProducts({ pr_uid }).subscribe({
          next: () => {
            alert('Produit supprimé avec succès');
            this.router.navigate(['/admin/view-all-products']);
          },
          error: (err) => {
            console.error(err);
          }
        });
      }
    }

    editProduct(productUid: string): void {
      this.router.navigate(['/admin/edit-products', productUid]);
    }

  }

