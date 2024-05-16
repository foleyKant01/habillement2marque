import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-read-single-product',
  templateUrl: './read-single-product.component.html',
  styleUrls: ['./read-single-product.component.scss']
})
export class ReadSingleProductComponent implements OnInit{

  product: any; // Stocke les détails du produit
  data: any;
  productUid: string | undefined;

  constructor(private route: ActivatedRoute, private http: BackService, private router: Router) {}

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      this.productUid = params['pr_uid']; // (+) converts string 'id' to a number
    });

    this.readSingleProducts();  }

  readSingleProducts(): void {
    let body = {
      pr_uid: this.productUid
    }
    this.http.ReadSingleProducts(body).subscribe({
      next: (response: any) => {
        this.product = response?.user; // Stocker les produits dans le tableau
        console.log(this.product)

      },
      error: (error) => {
        console.error('Failed to load products:', error);
      }
    });
      // }
    }

}
