import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-read-single-product',
  templateUrl: './read-single-product.component.html',
  styleUrls: ['./read-single-product.component.scss']
})
export class ReadSingleProductComponent implements OnInit{
  products: any;
  product: any; // Stocke les détails du produit
  data: any;
  productUid: string | undefined;
  productType: string | undefined;

  constructor(private route: ActivatedRoute, private http: BackService, private router: Router) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
      this.productType = params['type']; // (+) converts string 'id' to a number
    });

    this.readSingleProducts();
    this.allSimilarProducts();
  }
  readsingleProducts(pr_uid: number, type: string): void {
    this.router.navigate(['/user/read-single-product', pr_uid, type]);
  }

  readSingleProducts(): void {
    let body = {
      pr_uid: this.productUid
    }
    this.http.ReadSingleProducts(body).subscribe({
      next: (response: any) => {
        this.product = response?.user; // Stocker les produits dans le tableau

      },
      error: (error) => {
        console.error('Failed to load products:', error);
      }
    });

    }


    allSimilarProducts(): void {
      let body = {
        type: this.productType,
        pr_uid: this.productUid
      }
      this.http.AllSimilarProducts(body).subscribe({
        next: (response: any) => {
          this.products = response || []; // Stocker les produits dans le tableau
          if(response?.products)  {
            this.data = response?.products
            console.log(this.data)
          }
        },
        error: (error) => {
          console.error('Failed to load products:', error);
        }
      });
      }
}
