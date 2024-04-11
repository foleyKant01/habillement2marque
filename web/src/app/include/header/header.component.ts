import { Component,HostListener,ElementRef, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit{
  isNavbarWhite = false;
  activeLinkIndex = -1;

  setActiveLink(index: number) {
    this.activeLinkIndex = index;
  }

  constructor(private el: ElementRef) {}

  @HostListener('window:scroll', [])
  onWindowScroll() {
    if (window.scrollY > 0) {
      this.isNavbarWhite = true;
    } else {
      this.isNavbarWhite = false;
    }
  }

  ngOnInit(): void {
    throw new Error('Method not implemented.');
  }

}
