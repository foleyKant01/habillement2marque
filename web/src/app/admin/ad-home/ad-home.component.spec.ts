import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdHomeComponent } from './ad-home.component';

describe('AdHomeComponent', () => {
  let component: AdHomeComponent;
  let fixture: ComponentFixture<AdHomeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AdHomeComponent]
    });
    fixture = TestBed.createComponent(AdHomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
