import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router, RouterOutlet } from '@angular/router';
import { BackService } from 'src/app/back.service';

@Component({
  selector: 'app-create-products',
  templateUrl: './create-products.component.html',
  styleUrls: ['./create-products.component.scss']
})
export class CreateProductsComponent implements OnInit {

  loading= false;
  delayDuration= 2000
  success = false;

  ngOnInit(): void {
    // throw new Error('Method not implemented.');
  }

  constructor(private router: Router, private http: BackService){}

  createproducts: FormGroup = new FormGroup(
    {
      name: new FormControl(null, Validators.required),
      description: new FormControl(null, Validators.required),
      price: new FormControl(null, Validators.required),
      image: new FormControl(null, Validators.required),
      taille1: new FormControl(null, Validators.required),
      taille2: new FormControl(null, Validators.required),
      taille3: new FormControl(null, Validators.required),
      taille4: new FormControl(null, Validators.required),
    }
  )

  Createproducts(){
    if (this.createproducts.valid) {
      this.loading = true;

    this.http.CreateProducts(this.createproducts.value).subscribe({
      next : (reponse:any)=>{
        console.log(reponse);
        setTimeout(() => {
          this.loading = false;
          this.success = true;
          window.location.reload();
        }, this.delayDuration);

      },
      error: (error) => {
        console.error(error);
        setTimeout(() => {
          this.loading = false;
        }, this.delayDuration); // Désactiver le spinner en cas d'erreur
      }
    })
    }
  }


}
