import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http'; // Importez HttpClientModule


import { AdminRoutingModule } from './admin-routing.module';
import { AdminComponent } from './admin.component';
import { CreateProductsComponent } from './create-products/create-products.component';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { SpinnerComponent } from './spinner/spinner.component';
import { BackService } from '../back.service';
import { AdHomeComponent } from './ad-home/ad-home.component';
import { EditProductsComponent } from './edit-products/edit-products.component';
import { ViewAllProductsComponent } from './view-all-products/view-all-products.component';
import { ViewSingleProductsComponent } from './view-single-products/view-single-products.component';
import { DeleteProductsComponent } from './delete-products/delete-products.component';


@NgModule({
  declarations: [
    AdminComponent,
    CreateProductsComponent,
    SpinnerComponent,
    AdHomeComponent,
    EditProductsComponent,
    ViewAllProductsComponent,
    ViewSingleProductsComponent,
    DeleteProductsComponent,
  ],
  imports: [
    FormsModule,
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
