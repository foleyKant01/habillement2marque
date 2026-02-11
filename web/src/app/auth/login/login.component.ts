import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  ngOnInit(): void {
    // throw new Error('Method not implemented.');
  }

  constructor(private router: Router, private http: BackService){}

  loginuser: FormGroup = new FormGroup(
    {
      ad_email: new FormControl('', Validators.required),
      ad_password: new FormControl('', Validators.required),
    }
  )

  Loginadmin() {
  this.http.LoginAdmin(this.loginuser.value).subscribe({
    next: (reponse: any) => {
      console.log(reponse);

      if (reponse.status === 'success') {

        // 🔐 Sauvegarde du token
        localStorage.setItem('admin_infos', JSON.stringify(reponse.admin));

        // 🔁 Redirection vers le module ADMIN
        this.router.navigate(['admin']);

      } else {
        alert(reponse.message || 'Identifiants incorrects');
      }
    },
    error: (err) => {
      console.error(err);
      alert('Erreur serveur');
    }
  });
}


}
