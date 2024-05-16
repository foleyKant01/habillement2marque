import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DeleteProductsComponent } from './delete-products.component';

describe('DeleteProductsComponent', () => {
  let component: DeleteProductsComponent;
  let fixture: ComponentFixture<DeleteProductsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DeleteProductsComponent]
    });
    fixture = TestBed.createComponent(DeleteProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
