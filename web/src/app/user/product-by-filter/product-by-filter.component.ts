import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-product-by-filter',
  templateUrl: './product-by-filter.component.html',
  styleUrls: ['./product-by-filter.component.scss']
})
export class ProductByFilterComponent implements OnInit{

  products: any;
  product: any; // Stocke les détails du produit
  data: any;
  types: any;
  productUid: string | undefined;
  productType: string | undefined;

  constructor(private route: ActivatedRoute, private http: BackService, private router: Router) {}


  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productType = params['type']; // (+) converts string 'id' to a number
      console.log(this.productType);

      // this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
    });
    this.allSimilarTypeProducts();

  }

  readsingleProducts(pr_uid: number, type: string): void {
    this.router.navigate(['/user/read-single-product', pr_uid, type]);
  }


  allSimilarTypeProducts(): void {
    let body = {
      type: this.productType,
    }
    this.http.AllSimilarTypeProducts(body).subscribe({
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
