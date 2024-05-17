import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductByFilterComponent } from './product-by-filter.component';

describe('ProductByFilterComponent', () => {
  let component: ProductByFilterComponent;
  let fixture: ComponentFixture<ProductByFilterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ProductByFilterComponent]
    });
    fixture = TestBed.createComponent(ProductByFilterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
