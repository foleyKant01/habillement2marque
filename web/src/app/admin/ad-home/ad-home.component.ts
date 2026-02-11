import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-ad-home',
  templateUrl: './ad-home.component.html',
  styleUrls: ['./ad-home.component.scss']
})
export class AdHomeComponent implements OnInit {

admin: any;

ngOnInit(): void {
  const data = localStorage.getItem('admin_infos');
  if (data) {
    this.admin = JSON.parse(data);
  } else {
    console.warn('Aucun admin connecté');
  }  }

}
