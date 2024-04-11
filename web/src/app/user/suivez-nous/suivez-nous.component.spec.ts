import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SuivezNousComponent } from './suivez-nous.component';

describe('SuivezNousComponent', () => {
  let component: SuivezNousComponent;
  let fixture: ComponentFixture<SuivezNousComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SuivezNousComponent]
    });
    fixture = TestBed.createComponent(SuivezNousComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
