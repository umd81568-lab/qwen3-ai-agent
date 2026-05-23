# Qwen3 AI Agent - VPS Multi-Model System

A comprehensive AI agent system for managing multiple models on a VPS with hierarchical permission control.

## 🤖 System Architecture

### Primary Agent: Queen Model
- **Full Access**: All ports and commands
- **Location**: `/root/queen-model/`
- **Permission**: Execute freely, confirm only for modifications
- **Responsibility**: Main operations and system control

### Secondary Agents
1. **Hybrid Agent Project** (`/root/hybrid_agent_project/`)
2. **Local Models** (`/root/local/`)

**Permissions**: 
- ✅ Read-only operations
- ⚠️ Require confirmation for modifications/deletions
- ❌ No destructive operations allowed

## 📋 Files

- `vps_agent_config.md` - Configuration and permission levels
- `queen_model_agent.py` - Primary agent implementation
- `secondary_agent_control.py` - Secondary agent restrictions
- `agent_logs.json` - Command execution logs

## 🚀 Quick Start

```bash
# Initialize Queen Model Agent
python3 queen_model_agent.py

# Use Secondary Agent Control
python3 secondary_agent_control.py
```

## 📊 VPS Resources

- **OS**: Ubuntu Linux
- **Python**: 3.12
- **GPU**: NVIDIA CUDA 13
- **Models**:
  - Queen Model (Hugging Face)
  - Hybrid Agent Project
  - Local Models (2-part safetensors)

## 🔐 Security Features

1. **Permission Hierarchy**: Different access levels for primary/secondary agents
2. **Command Logging**: All commands logged with timestamp and status
3. **Confirmation Prompts**: Critical operations require user approval
4. **Validation**: Commands validated against forbidden operation list
5. **Timeout Protection**: 30-second timeout for all commands

## 📝 Command Execution Flow

```
User Request
    ↓
Agent Selection (Primary/Secondary)
    ↓
Permission Check
    ↓
Command Validation
    ↓
User Confirmation (if required)
    ↓
Command Execution
    ↓
Logging & Result
```

## 🔄 Updates

All changes are tracked in Git commits with GPG verification.

**Current Setup**: 2026-05-23
- Queen Model Primary Agent ✅
- Secondary Agent Control ✅
- Permission System ✅