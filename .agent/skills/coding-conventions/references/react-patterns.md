# React Implementation Patterns

## 1. Functional Components & Hooks
- **Functional Components**: Use functional components by default for all UI elements.
- **Hooks**: Use standard React hooks (`useState`, `useEffect`, `useMemo`, `useCallback`) for interactivity and side effects.

**Rule**: Keep components pure and side-effect free whenever possible. Isolate side effects to `useEffect` or custom hooks.

## 2. Component Props
Always use TypeScript interfaces to define props. Suffix the interface with `Props`.

```tsx
interface ProfileCardProps {
  userId: string;
  userName: string;
  isAdmin?: boolean; // Optional prop
}

const ProfileCard = ({ userId, userName, isAdmin = false }: ProfileCardProps): React.ReactElement => {
  return (
    <div>{userName}</div>
  );
};
```

## 3. Fragment Usage
Use `<>...</>` to group elements without adding extra nodes to the DOM.

```tsx
// ✅ Good
return (
  <>
    <Header />
    <MainContent />
  </>
);
```

## 4. Key Prop in Lists
Never use array index as a `key` if the list can change. Use unique IDs.

```tsx
// ✅ Good
{users.map((user) => (
  <UserItem key={user.id} data={user} />
))}
```

## 5. Tailwind CSS Strategy
- Use utility classes directly in `className`.
- Use `clsx` or `tailwind-merge` for conditional classes.
- Avoid using `@apply` in CSS files unless creating a very common reusable base.

```tsx
import { cn } from '@/lib/utils'; // utility using tailwind-merge

const Button = ({ active }: { active: boolean }) => (
  <button className={cn('px-4 py-2', active ? 'bg-blue-500' : 'bg-gray-200')}>
    Click Me
  </button>
);
```

## 6. Data Fetching & Mutations
Use tools like React Query, SWR, or standard `fetch` API within hooks or event handlers for data operations. Extract data fetching logic into custom hooks.

```ts
export const useUserProfile = (userId: string) => {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });
}
```

## 7. Loading & Error States
Always implement loading states and error handling for a better user experience during data fetching. Use React `<Suspense>` combined with Error Boundaries where appropriate.
