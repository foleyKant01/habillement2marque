import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { UserRoutingModule } from './user-routing.module';
import { UserComponent } from './user.component';
import { HomeComponent } from './home/home.component';
import { HeaderComponent } from '../include/header/header.component';
import { FooterComponent } from '../include/footer/footer.component';
import { ContactComponent } from './contact/contact.component';
import { SuivezNousComponent } from './suivez-nous/suivez-nous.component';


@NgModule({
  declarations: [
    UserComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    ContactComponent,
    SuivezNousComponent,
  ],
  imports: [
    CommonModule,
    UserRoutingModule,

  ]
})
export class UserModule { }
