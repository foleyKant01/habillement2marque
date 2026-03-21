import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit{
  products: any[] = []; // Tableau pour stocker les produits
  data: any;

  showModal = false;
  selectedSize: string = '';
  selectedColor: string = '';
  currentProduct: any = null; 

  colors: string[] = ['Noir', 'Blanc', 'Gris', 'Marron', 'Beige', 'Bleu marine', 'Rouge', 'Vert', 'Jaune', 'Bleu', 'Rose', 'Violet', 'Orange', 'Multi'];


  constructor(private router: Router, private route: ActivatedRoute, private http: BackService) { }

  ngOnInit(): void {
    this.viewallProducts()
  }

  readsingleProducts(pr_uid: number, type: string, name: string): void {
    this.router.navigate(['/user/read-single-product', pr_uid, type, name]);
  }

  openOrderModal(product: any) {
  this.currentProduct = product;
    if (
      product.type === 'Chaussures Homme' ||
      product.type === 'Chaussures Femme'
    ) {
      this.showModal = true;
    } else {
      this.sendToWhatsApp(product);
    }
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

  sendToWhatsApp(product: any) {
    let message = `Bonjour je suis intéressé par ce produit\n
    Nom: ${product.name}\n
    Ref: ${product.pr_uid}\n
    Prix: ${product.price} FCFA \n`;

      if (this.selectedSize ) {
        if (this.selectedColor) {
          message += `\nPointure: ${this.selectedSize}, \nCouleur: ${this.selectedColor}`;
        }
      }

      const url = `https://wa.me/2250777861623?text=${encodeURIComponent(message)}`;
      window.open(url, '_blank');

      this.showModal = false;
      this.selectedSize = '';
      this.selectedColor = '';
  }

}
