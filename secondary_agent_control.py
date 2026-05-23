#!/usr/bin/env python3
"""
Secondary Agent Control System
Restricted permissions for Hybrid Agent and Local Models
"""

import subprocess
from typing import Tuple

class SecondaryAgent:
    """Secondary AI Agent with restricted permissions"""
    
    def __init__(self, agent_name: str, agent_path: str):
        self.agent_name = agent_name
        self.agent_path = agent_path
        self.is_primary = False
        self.allowed_operations = [
            'read',
            'list',
            'query',
            'infer',
            'analyze'
        ]
        self.forbidden_operations = [
            'delete',
            'rm',
            'rmdir',
            'truncate',
            'dd',
            'mkfs'
        ]
    
    def ask_permission(self, command: str, operation: str) -> bool:
        """Ask permission for restricted operations"""
        print("\n" + "="*60)
        print(f"⚠️  SECONDARY AGENT PERMISSION REQUEST")
        print("="*60)
        print(f"Agent: {self.agent_name}")
        print(f"Operation: {operation.upper()}")
        print(f"Command: {command}")
        print("="*60)
        
        response = input("Approve? (yes/no): ").strip().lower()
        return response in ['yes', 'y']
    
    def validate_command(self, command: str) -> Tuple[bool, str]:
        """Validate command against permission rules"""
        
        # Check for forbidden operations
        for forbidden in self.forbidden_operations:
            if forbidden in command:
                return False, f"❌ Operation '{forbidden}' is forbidden for secondary agents"
        
        # Check for modification operations
        if any(op in command for op in ['mv', 'cp', 'sed', 'echo >', 'write']):
            return True, "requires_permission"
        
        return True, "allowed"
    
    def execute_command(self, command: str) -> Tuple[bool, str]:
        """Execute command with validation"""
        
        # Validate command
        is_valid, validation_status = self.validate_command(command)
        
        if not is_valid:
            return False, validation_status
        
        # Ask permission if required
        if validation_status == "requires_permission":
            operation = command.split()[0]
            if not self.ask_permission(command, operation):
                return False, "❌ Command execution denied by user"
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                return True, result.stdout
            else:
                return False, result.stderr
                
        except Exception as e:
            return False, f"❌ Error: {str(e)}"

class AgentManager:
    """Manage multiple secondary agents"""
    
    def __init__(self):
        self.agents = {}
    
    def register_agent(self, agent_name: str, agent_path: str):
        """Register a secondary agent"""
        self.agents[agent_name] = SecondaryAgent(agent_name, agent_path)
        print(f"✅ Agent '{agent_name}' registered")
    
    def execute_on_agent(self, agent_name: str, command: str) -> Tuple[bool, str]:
        """Execute command on specific agent"""
        if agent_name not in self.agents:
            return False, f"❌ Agent '{agent_name}' not found"
        
        agent = self.agents[agent_name]
        return agent.execute_command(command)

# Example usage
if __name__ == "__main__":
    manager = AgentManager()
    
    # Register secondary agents
    manager.register_agent("hybrid_agent", "/root/hybrid_agent_project/")
    manager.register_agent("local_models", "/root/local/")
    
    print("\n🔒 Secondary Agent Control System Initialized")
    print("⚠️  Destructive operations require permission")