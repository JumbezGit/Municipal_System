# Municipal Tax System Deployment (Render + Vercel)

## Architecture
- Backend: Django API on Render
- Database: PostgreSQL on Render
- Frontend: React (Vite) on Vercel

## 1. Deploy Backend to Render

### Option A (recommended): Blueprint deploy
1. Push this repository to GitHub.
2. In Render, click `New +` -> `Blueprint`.
3. Select this repository.
4. Render will read [`render.yaml`](./render.yaml) and create:
- `municipal-tax-backend` web service
- `municipal-tax-db` PostgreSQL database
5. After first deploy, open backend service -> `Environment` and update:
- `ALLOWED_HOSTS` to your actual Render hostname
- `FRONTEND_URL` to your Vercel frontend URL

### Option B: Manual web service setup
If you deploy manually in Render:
- Root directory: `backend`
- Build command: `./build.sh`
- Start command: `gunicorn municipal_tax.wsgi:application --bind 0.0.0.0:$PORT`
- Runtime: Python 3

Set backend environment variables:
- `SECRET_KEY`: long random value
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `your-backend.onrender.com`
- `DATABASE_URL`: Render PostgreSQL internal/external URL
- `FRONTEND_URL`: `https://your-frontend.vercel.app`

## 2. Deploy Frontend to Vercel
1. Import the same GitHub repository into Vercel.
2. Set `Root Directory` to `frontend`.
3. Build settings:
- Framework preset: `Vite`
- Build command: `npm run build`
- Output directory: `dist`
4. Add environment variable:
- `VITE_API_URL=https://your-backend.onrender.com/api`
5. Deploy.

`frontend/vercel.json` is included to rewrite SPA routes to `index.html`.

## 3. Connect Both Sides
After Vercel gives you a domain:
1. Update backend `FRONTEND_URL` in Render to the Vercel URL.
2. Confirm backend `ALLOWED_HOSTS` contains the Render hostname.
3. Redeploy backend (or trigger manual deploy).

## 4. Health Check
Use these checks after deployment:
- Backend root admin: `https://your-backend.onrender.com/admin/`
- API login endpoint: `https://your-backend.onrender.com/api/auth/login/`
- Frontend app: `https://your-frontend.vercel.app`

## Files Added/Updated for Deployment
- [`render.yaml`](./render.yaml)
- [`backend/municipal_tax/deployment.py`](./backend/municipal_tax/deployment.py)
- [`backend/.env.example`](./backend/.env.example)
- [`frontend/.env.example`](./frontend/.env.example)
- [`frontend/vercel.json`](./frontend/vercel.json)
