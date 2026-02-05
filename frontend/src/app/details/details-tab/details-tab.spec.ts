import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DetailsTab } from './details-tab';

describe('DetailsTab', () => {
  let component: DetailsTab;
  let fixture: ComponentFixture<DetailsTab>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DetailsTab]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DetailsTab);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
