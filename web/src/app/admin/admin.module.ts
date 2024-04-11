import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http'; // Importez HttpClientModule


import { AdminRoutingModule } from './admin-routing.module';
import { AdminComponent } from './admin.component';
import { CreateProductsComponent } from './create-products/create-products.component';
import { ReactiveFormsModule } from '@angular/forms';
import { SpinnerComponent } from './spinner/spinner.component';
import { BackService } from '../back.service';
import { AdHomeComponent } from './ad-home/ad-home.component';


@NgModule({
  declarations: [
    AdminComponent,
    CreateProductsComponent,
    SpinnerComponent,
    AdHomeComponent,
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule,
    AdminRoutingModule,
    HttpClientModule
  ],
  providers: [
    BackService // Ajoutez BackService aux providers
  ]
})
export class AdminModule { }
