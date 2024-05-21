import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { UserComponent } from './user.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from '../include/header/header.component';
import { FooterComponent } from '../include/footer/footer.component';
import { SuivezNousComponent } from './suivez-nous/suivez-nous.component';
import { ReadSingleProductComponent } from './read-single-product/read-single-product.component';
import { ProductByFilterComponent } from './product-by-filter/product-by-filter.component';
import { OffresComponent } from './offres/offres.component';


@NgModule({
  declarations: [
    UserComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    OffresComponent,
    SuivezNousComponent,
    ReadSingleProductComponent,
    ProductByFilterComponent,
    OffresComponent,
  ],
  imports: [
    CommonModule,
    UserRoutingModule,

  ]
})
export class UserModule { }
