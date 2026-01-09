import { CategorySchema } from './categories.model';

describe('CategoriesModel', () => {
  it('should create an instance', () => {
    expect(CategorySchema.parse({
      id: '1',
      name: 'Category 1',
      level: 1,
      parent_ids: []
    })).toBeTruthy();
  });
});
  