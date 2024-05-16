import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NosArticlesComponent } from './nos-articles.component';
import { ChaussuresComponent } from './chaussures/chaussures.component';
import { MontresComponent } from './montres/montres.component';

const routes: Routes = [
  { path:'', component: NosArticlesComponent,
  children: [
    { path:'', redirectTo:'chaussures', pathMatch:'full' },
    { path:'chaussures', component: ChaussuresComponent },
    { path:'montres', component: MontresComponent },
    // {path: 'nos-articles', loadChildren: () => import('./nos-articles/nos-articles.module').then((m) => m.NosArticlesModule)},

  ]
}
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class NosArticlesRoutingModule { }
