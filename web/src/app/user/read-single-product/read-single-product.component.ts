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
  products_color: any;
  product: any; // Stocke les détails du produit
  data: any;
  data_color: any;
  productUid: string | undefined;
  productType: string | undefined;
  productName: string | undefined;

  constructor(private route: ActivatedRoute, private http: BackService, private router: Router) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
      this.productType = params['type']; // (+) converts string 'id' to a number
      this.productName = params['name']; // (+) converts string 'id' to a number
    });

    this.readSingleProducts();
    this.allSimilarProducts();
    this.allSimilarColorProducts();
  }
  readsingleProducts(pr_uid: number, type: string, name: string): void {
    this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
      this.router.navigate(['/user/read-single-product', pr_uid, type, name]));
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
        name: this.productName,
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

      allSimilarColorProducts(): void {
      let body = {
        name: this.productName,
        pr_uid: this.productUid
      }
      this.http.AllSimilarColorProducts(body).subscribe({
        next: (response: any) => {
          this.products_color = response || []; // Stocker les produits dans le tableau
          if(response?.products_color)  {
            this.data_color = response?.products_color
            console.log(this.data_color)
          }
        },
        error: (error) => {
          console.error('Failed to load products:', error);
        }
      });
      }
}
