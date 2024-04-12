import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-view-all-products',
  templateUrl: './view-all-products.component.html',
  styleUrls: ['./view-all-products.component.scss']
})
export class ViewAllProductsComponent implements OnInit {
  products: any[] = []; // Tableau pour stocker les produits
  data: any;

  constructor(private router: Router, private route: ActivatedRoute, private http: BackService) { }

  ngOnInit(): void {
    this.viewallProducts(); // Charger les produits au chargement du composant
  }

  viewallProducts(): void {
    this.http.ReadAllProducts().subscribe({
      next: (response: any) => {
        this.products = response || []; // Stocker les produits dans le tableau
        if(response?.products)  {
          this.data = response?.products
          // console.log(this.data)

        }
      },
      error: (error) => {
        console.error('Failed to load products:', error);
      }
    });
  }

  editProduct(pr_uid: number): void {
    this.router.navigate(['/admin/edit-products', pr_uid]);
  }

}
