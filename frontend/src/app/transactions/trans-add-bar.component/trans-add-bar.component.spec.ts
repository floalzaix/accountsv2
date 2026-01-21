import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TransAddBarComponent } from './trans-add-bar.component';

describe('TransAddBarComponent', () => {
  let component: TransAddBarComponent;
  let fixture: ComponentFixture<TransAddBarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TransAddBarComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TransAddBarComponent);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
