import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NotfoundComponent } from './notfound/notfound.component';
import { AppComponent } from './app.component';

const routes: Routes = [
  { path:'', component: AppComponent,
  children: [
  { path: '', redirectTo: 'user', pathMatch: 'full' },
  {path: 'user', loadChildren: () => import('./user/user.module').then((m) => m.UserModule)},
  {path: 'admin', loadChildren: () => import('./admin/admin.module').then((m) => m.AdminModule)},
  {path: 'auth', loadChildren: () => import('./auth/auth.module').then((m) => m.AuthModule)},
  // {
  //   path: 'auth',
  //   loadChildren: () => import('./auth/auth.module').then((m) => m.AuthModule)
  // },
  // {
  //   path: 'admin',
  //   loadChildren: () => import('./admin/admin.module').then((m) => m.AdminModule)
  // },
  // {
  //   path: 'super-admin',
  //   loadChildren: () => import('./super-admin/super-admin.module').then((m) => m.SuperAdminModule)
  // },
  { path: '**', component: NotfoundComponent }
  ]
}
];
@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
