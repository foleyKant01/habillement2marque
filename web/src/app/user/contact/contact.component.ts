import { Component } from '@angular/core';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss']
})
export class ContactComponent {

  contact = {
    fullName: '',
    email: '',
    message: ''
  };

  submitForm() {
    console.log('Formulaire soumis :', this.contact);
    // Ajoutez ici la logique pour envoyer le formulaire de contact (par exemple, en utilisant un service HTTP)
    // Réinitialisez le formulaire après l'envoi si nécessaire
    this.contact = {
      fullName: '',
      email: '',
      message: ''
    };
  }

}
