import {useItems} from '../hooks/useItems.ts'; // or .tsx
import { Item, ItemCreate } from '@/types/item';
import { useState } from 'react';

export default function InventoryPage() {
  const { data: items = [], isLoading } = useItems();
  const createItem = useCreateItem();

  const [form, setForm] = useState<ItemCreate>({
    name: '',
    price: 0,
    stock: 0,
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    createItem.mutate(form, {
      onSuccess: () => {
        setForm({ name: '', price: 0, stock: 0 });
      },
    });
  };

  if (isLoading) return <div className="p-8">Loading...</div>;

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-8">Inventory</h1>

      <form onSubmit={handleSubmit} className="mb-12 bg-white p-6 rounded-lg shadow-sm">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
          <input
            type="text"
            placeholder="Product name"
            value={form.name}
            onChange={e => setForm({ ...form, name: e.target.value })}
            className="border rounded px-3 py-2"
            required
          />
          <input
            type="number"
            placeholder="Price"
            value={form.price || ''}
            onChange={e => setForm({ ...form, price: Number(e.target.value) })}
            className="border rounded px-3 py-2"
            required
            step="0.01"
          />
          <input
            type="number"
            placeholder="Initial stock"
            value={form.stock || ''}
            onChange={e => setForm({ ...form, stock: Number(e.target.value) })}
            className="border rounded px-3 py-2"
            required
          />
          <button
            type="submit"
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
            disabled={createItem.isLoading}
          >
            {createItem.isLoading ? 'Adding...' : 'Add Item'}
          </button>
        </div>
      </form>

      <div className="bg-white rounded-lg shadow-sm overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Name</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Price</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Stock</th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {items.map(item => (
              <tr key={item.id}>
                <td className="px-6 py-4 whitespace-nowrap">{item.name}</td>
                <td className="px-6 py-4 whitespace-nowrap">₦{item.price.toFixed(2)}</td>
                <td className="px-6 py-4 whitespace-nowrap">{item.stock}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
