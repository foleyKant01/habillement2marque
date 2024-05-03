import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse, HttpHeaders } from '@angular/common/http'
import { Observable, catchError, pipe, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BackService {


  private apiUrl = 'mysql+pymysql://root:@localhost/tt_officiel';


  constructor(private http: HttpClient, private api: HttpClient) {}


  // Api Admin

  CreateAdmin(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }
    return this.http.post("http://127.0.0.1:5000/api/admin/create", body, httpOptions)
  }


  LoginAdmin(body:any): Observable<any> {
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }
    return this.http.post('http://127.0.0.1:5000/api/admin/login', body, httpOptions);
    // return this.api.post('mysql+pymysql://root:@localhost/tt_officiel', body, httpOptions)
  }


  // ReadAllUser(): Observable<any>{
  //   return this.api.get<any>("http://127.0.0.1:5000/api/user/readall")
  // }


  // ReadSingleUser(u_uid:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.get("http://127.0.0.1:5000/api/user/readsingle/${u_uid}", httpOptions);
  // }

  // UpdateUser(body:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.patch("http://127.0.0.1:5000/api/user/update", body, httpOptions)
  // }


  // DeleteUser(body:any){

  //   const httpOptions = {
  //     headers: new HttpHeaders({
  //     'Content-Type': 'application/json',
  //     })
  //   };

  //   return this.api.post("http://127.0.0.1:5000/api/user/delete", body, httpOptions)
  // }


  // Api Products

   ReadAllProducts(): Observable<any>{
    return this.http.get<any[]>("http://127.0.0.1:5000/api/products/readall")
  }

  // ReadSingleProducts(pr_uid: string): Observable<any> {
  //   const url = `http://127.0.0.1:5000/api/products/readsingle/${pr_uid}`;
  //   return this.http.get(url); // Utilisation correcte de la méthode get sans les arguments supplémentaires
  // }



  ReadSingleProducts(body : any){
    const httpOptions = {
      headers: new HttpHeaders({
      'Content-Type': 'application/json',
      Authorization: ''
      }),
    };
    return this.http.post("http://127.0.0.1:5000/api/products/readsingle",body, httpOptions);
  }


  CreateProducts(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
      })
    }
    return this.http.post("http://127.0.0.1:5000/api/products/create", body, httpOptions)
  }



  DeleteProducts(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
      'Content-Type': 'application/json',
      })
    };
    return this.http.delete("http://127.0.0.1:5000/api/products/delete", body)
  }


  UpdateProducts(body:any){
    const httpOptions = {
      headers: new HttpHeaders({
      'Content-Type': 'application/json',
      })
    };
    return this.http.patch("http://127.0.0.1:5000/api/products/update", body, httpOptions)
  }
}
