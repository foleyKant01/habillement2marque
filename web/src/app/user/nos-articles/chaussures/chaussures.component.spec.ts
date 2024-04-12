import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChaussuresComponent } from './chaussures.component';

describe('ChaussuresComponent', () => {
  let component: ChaussuresComponent;
  let fixture: ComponentFixture<ChaussuresComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ChaussuresComponent]
    });
    fixture = TestBed.createComponent(ChaussuresComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
