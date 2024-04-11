import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AdminComponent } from './admin.component';
import { HomeComponent } from '../user/home/home.component';
import { CreateProductsComponent } from './create-products/create-products.component';
import { AdHomeComponent } from './ad-home/ad-home.component';

const routes: Routes = [
  { path:'', component: AdminComponent,
  children: [
    { path:'', redirectTo:'home', pathMatch:'full' },
    { path:'ad-home', component: AdHomeComponent },
    { path:'create-products', component: CreateProductsComponent },
  ]
  }
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AdminRoutingModule { }
