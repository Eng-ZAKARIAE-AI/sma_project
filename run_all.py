import subprocess
import sys
import time
import os

def run_backend():
    print("🚀 Démarrage du Backend...")
    return subprocess.Popen(
        [sys.executable, "-m", "backend.app.api"],
        env={**os.environ, "PYTHONPATH": "."}
    )

def run_frontend():
    print("🎨 Démarrage du Frontend (Streamlit)...")
    return subprocess.Popen(
        [sys.executable, "-m", "streamlit", "run", "frontend/app.py"]
    )

if __name__ == "__main__":
    backend_proc = None
    frontend_proc = None
    try:
        backend_proc = run_backend()
        # Laisser un peu de temps au backend pour démarrer
        time.sleep(3)
        
        frontend_proc = run_frontend()
        
        print("\n✅ Les deux services sont en cours d'exécution.")
        print("   - Backend : http://127.0.0.1:8000")
        print("   - Frontend : http://localhost:8501 (par défaut)")
        print("\nAppuyez sur Ctrl+C pour arrêter les deux services.")
        
        while True:
            time.sleep(1)
            if backend_proc.poll() is not None:
                print("❌ Le processus Backend s'est arrêté de manière inattendue.")
                break
            if frontend_proc.poll() is not None:
                print("❌ Le processus Frontend s'est arrêté de manière inattendue.")
                break
                
    except KeyboardInterrupt:
        print("\n🛑 Arrêt des services...")
    finally:
        if backend_proc:
            backend_proc.terminate()
        if frontend_proc:
            frontend_proc.terminate()
        print("👋 Au revoir !")
