export interface Item {
  id: number;
  name: string;
  barcode?: string;
  price: number;
  stock: number;
  created_at: string;
}

export interface ItemCreate {
  name: string;
  barcode?: string;
  price: number;
  stock: number;
}

export interface ItemUpdate {
  name?: string;
  barcode?: string;
  price?: number;
  stock?: number;
}
