import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NosArticlesComponent } from './nos-articles.component';

describe('NosArticlesComponent', () => {
  let component: NosArticlesComponent;
  let fixture: ComponentFixture<NosArticlesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NosArticlesComponent]
    });
    fixture = TestBed.createComponent(NosArticlesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
