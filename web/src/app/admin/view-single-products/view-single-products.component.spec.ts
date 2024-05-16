import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewSingleProductsComponent } from './view-single-products.component';

describe('ViewSingleProductsComponent', () => {
  let component: ViewSingleProductsComponent;
  let fixture: ComponentFixture<ViewSingleProductsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ViewSingleProductsComponent]
    });
    fixture = TestBed.createComponent(ViewSingleProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
