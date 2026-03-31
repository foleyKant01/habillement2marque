import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http'
import { Observable, catchError, pipe, throwError } from 'rxjs';
// import { environment } from './environments/environment.prod';
import { environment } from './environments/environment';

@Injectable({
  providedIn: 'root'
})
export class BackService {

  private apiUrl = 'mysql+pymysql://root:@localhost/tt_officiel';
  api_url = environment.apiUrl

  constructor(private https: HttpClient, private api: HttpClient) {}

  // Api Admin

  CreateAdmin(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }
    return this.https.post(this.api_url+"/api/admin/create", body, httpOptions)
  }

  LoginAdmin(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }
    return this.https.post(this.api_url+"/api/admin/login", body, httpOptions);
  }

  // ReadAllUser(): Observable<any>{
  //   return this.api.get<any>(this.api_url+"/api/user/readall")
  // }

  // ReadSingleUser(u_uid:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.get(this.api_url+"/api/user/readsingle/${u_uid}", httpOptions);
  // }

  // UpdateUser(body:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.patch(this.api_url+"/api/user/update", body, httpOptions)
  // }


  // DeleteUser(body:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.post(this.api_url+"/api/user/delete", body, httpOptions)
  // }


  // Api Products

   ReadAllProducts(): Observable<any>{
    return this.https.get<any[]>(this.api_url+"/api/products/readall")
  }


  ReadSingleProducts(body : any){
    return this.https.post(this.api_url+"/api/products/readsingle",body);
  }


  AllSimilarProducts(body : any){
    return this.https.post(this.api_url+"/api/products/readsimilar",body);
  }

  AllSimilarColorProducts(body : any){
    return this.https.post(this.api_url+"/api/products/readsimilarcolor",body);
  }


  AllSimilarTypeProducts(body : any){
    return this.https.post(this.api_url+"/api/products/readsimilartype",body);
  }

  CreateProducts(formData: FormData){
    // const httpOptions = {
    //   // headers: new HttpHeaders({
    //   //   'Content-Type': 'application/json',
    //   // })
    // }
    return this.https.post(this.api_url+"/api/products/create", formData)
  }

  DeleteProducts(body:any){
    return this.https.post(this.api_url+"/api/products/delete", body)
  }

  UpdateProducts(body:any){
    return this.https.post(this.api_url+"/api/products/update", body)
  }
}
