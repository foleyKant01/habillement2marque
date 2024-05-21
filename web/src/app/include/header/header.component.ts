import { Component,HostListener,ElementRef, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit{
  isNavbarWhite = false;
  activeLinkIndex = -1;
  selectedCategory: string | undefined;
  products: any[] = []; // Assurez-vous de définir correctement votre tableau de produits


  setActiveLink(index: number) {
    this.activeLinkIndex = index;
  }

  redirectToCategory(type: string): void {
    // this.selectedCategory = type;
    this.router.navigateByUrl('/', {skipLocationChange: true}).then(()=>
      this.router.navigate(['user/product_by_filter',type]));
  }

  constructor(private el: ElementRef, private route: ActivatedRoute, private http: BackService, private router: Router) {}

  @HostListener('window:scroll', [])
  onWindowScroll() {
    if (window.scrollY > 0) {
      this.isNavbarWhite = true;
    } else {
      this.isNavbarWhite = false;
    }
  }

  ngOnInit(): void {
    // throw new Error('Method not implemented.');
  }

}
