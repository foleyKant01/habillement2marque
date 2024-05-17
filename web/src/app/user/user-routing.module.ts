import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UserComponent } from './user.component';
import { HomeComponent } from './home/home.component';
import { ContactComponent } from './contact/contact.component';
import { SuivezNousComponent } from './suivez-nous/suivez-nous.component';
import { ReadSingleProductComponent } from './read-single-product/read-single-product.component';

const routes: Routes = [
  { path:'', component: UserComponent,
  children: [
    { path:'', redirectTo:'home', pathMatch:'full' },
    { path:'home', component: HomeComponent },
    { path:'read-single-product/:pr_uid/:type', component: ReadSingleProductComponent },
    { path:'contact', component: ContactComponent },
    { path:'suivez-nous', component: SuivezNousComponent },
    {path: 'nos-articles', loadChildren: () => import('./nos-articles/nos-articles.module').then((m) => m.NosArticlesModule)},
  ]
  }
];
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class UserRoutingModule { }
