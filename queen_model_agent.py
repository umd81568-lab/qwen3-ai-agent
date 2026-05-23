#!/usr/bin/env python3
"""
Queen Model Primary Agent
VPS Command Executor with Permission Control
"""

import os
import subprocess
import json
from datetime import datetime
from typing import Dict, List, Tuple

class QueenModelAgent:
    """Primary AI Agent for VPS Command Execution"""
    
    def __init__(self):
        self.model_path = "/root/queen-model/"
        self.venv_path = "/root/hybrid_agent_project/.venv"
        self.local_models = "/root/local/"
        self.logs = []
        self.is_primary = True
        
    def log_command(self, command: str, status: str, output: str = ""):
        """Log all executed commands"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "command": command,
            "status": status,
            "output": output[:500]  # Truncate long outputs
        }
        self.logs.append(log_entry)
        return log_entry
    
    def ask_permission(self, command: str, operation_type: str) -> bool:
        """
        Ask user permission for modifications/deletions
        operation_type: 'delete', 'modify', 'write'
        """
        print("\n" + "="*60)
        print(f"⚠️  PERMISSION REQUIRED")
        print("="*60)
        print(f"Operation Type: {operation_type.upper()}")
        print(f"Command: {command}")
        print("="*60)
        
        response = input("Do you approve? (yes/no): ").strip().lower()
        
        if response in ['yes', 'y']:
            print("✅ Permission granted")
            return True
        else:
            print("❌ Permission denied")
            return False
    
    def execute_command(self, command: str, require_permission: bool = False) -> Tuple[bool, str]:
        """Execute VPS command with safety checks"""
        
        # Check if destructive operation
        destructive_keywords = ['rm -rf', 'dd', 'mkfs', 'shutdown', 'reboot']
        is_destructive = any(keyword in command for keyword in destructive_keywords)
        
        # Require permission for destructive operations
        if is_destructive and require_permission:
            if not self.ask_permission(command, 'destructive'):
                return False, "❌ Command execution denied by user"
        
        # Check for modification operations
        modification_keywords = ['mv', 'cp', 'sed', 'echo >', 'nano', 'vim']
        is_modification = any(keyword in command for keyword in modification_keywords)
        
        if is_modification and not self.is_primary:
            if not self.ask_permission(command, 'modification'):
                return False, "❌ Modification denied for secondary agent"
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            status = "success" if result.returncode == 0 else "failed"
            output = result.stdout or result.stderr
            
            self.log_command(command, status, output)
            return True, output
            
        except subprocess.TimeoutExpired:
            self.log_command(command, "timeout")
            return False, "⏱️ Command timeout"
        except Exception as e:
            self.log_command(command, "error", str(e))
            return False, f"❌ Error: {str(e)}"
    
    def list_models(self) -> Dict:
        """List all available models on VPS"""
        models_info = {
            "queen_model": {
                "path": self.model_path,
                "type": "huggingface",
                "status": "active"
            },
            "hybrid_agent": {
                "path": "/root/hybrid_agent_project/",
                "type": "hybrid",
                "status": "active"
            },
            "local_models": {
                "path": self.local_models,
                "type": "local_safetensors",
                "status": "active"
            },
            "cuda": {
                "version": "13",
                "status": "available"
            }
        }
        return models_info
    
    def get_system_status(self) -> Dict:
        """Get VPS system status"""
        success, disk = self.execute_command("df -h / | tail -1")
        success, memory = self.execute_command("free -h | grep Mem")
        success, gpu = self.execute_command("nvidia-smi --query-gpu=memory.used,memory.total --format=csv,nounits,noheader")
        
        return {
            "disk": disk.strip() if success else "N/A",
            "memory": memory.strip() if success else "N/A",
            "gpu": gpu.strip() if success else "N/A"
        }
    
    def save_logs(self, filename: str = "agent_logs.json"):
        """Save execution logs to file"""
        with open(filename, 'w') as f:
            json.dump(self.logs, f, indent=2)
        return f"✅ Logs saved to {filename}"

# Example usage
if __name__ == "__main__":
    agent = QueenModelAgent()
    
    print("🤖 Queen Model Primary Agent Initialized")
    print(f"📍 Location: {agent.model_path}")
    print(f"⚡ Status: ACTIVE")
    print(f"🔐 Permission Level: FULL ACCESS\n")
    
    # List available models
    models = agent.list_models()
    print("📦 Available Models:")
    for model, info in models.items():
        print(f"  - {model}: {info.get('status', 'unknown')}")
    
    # Get system status
    print("\n📊 System Status:")
    status = agent.get_system_status()
    for key, value in status.items():
        print(f"  {key}: {value}")