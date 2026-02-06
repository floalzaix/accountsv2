import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MenuCol } from './menu-col';

describe('MenuCol', () => {
  let component: MenuCol;
  let fixture: ComponentFixture<MenuCol>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MenuCol]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MenuCol);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
