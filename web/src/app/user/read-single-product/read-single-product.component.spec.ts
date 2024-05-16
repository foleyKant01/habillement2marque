import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReadSingleProductComponent } from './read-single-product.component';

describe('ReadSingleProductComponent', () => {
  let component: ReadSingleProductComponent;
  let fixture: ComponentFixture<ReadSingleProductComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ReadSingleProductComponent]
    });
    fixture = TestBed.createComponent(ReadSingleProductComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
