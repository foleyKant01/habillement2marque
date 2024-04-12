import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminComponent } from './admin.component';
import { HomeComponent } from '../user/home/home.component';
import { CreateProductsComponent } from './create-products/create-products.component';
import { AdHomeComponent } from './ad-home/ad-home.component';
import { SpinnerComponent } from './spinner/spinner.component';
import { EditProductsComponent } from './edit-products/edit-products.component';
import { ViewAllProductsComponent } from './view-all-products/view-all-products.component';
import { ViewSingleProductsComponent } from './view-single-products/view-single-products.component';

const routes: Routes = [
  { path:'', component: AdminComponent,
  children: [
    { path:'', redirectTo:'home', pathMatch:'full' },
    { path:'ad-home', component: AdHomeComponent },
    { path:'create-products', component: CreateProductsComponent },
    { path:'edit-products', component: EditProductsComponent },
    { path:'spinner', component: SpinnerComponent },
    { path:'view-all-products', component: ViewAllProductsComponent },
    { path:'view-single-products', component: ViewSingleProductsComponent },
  ]
  }
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
