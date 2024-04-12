import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { NosArticlesRoutingModule } from './nos-articles-routing.module';
import { MontresComponent } from './montres/montres.component';
import { ChaussuresComponent } from './chaussures/chaussures.component';


@NgModule({
  declarations: [
    MontresComponent,
    ChaussuresComponent
  ],
  imports: [
    CommonModule,
    NosArticlesRoutingModule
  ]
})
export class NosArticlesModule { }
