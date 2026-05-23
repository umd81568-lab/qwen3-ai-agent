# VPS AI Agent Configuration

## Primary Agent: Queen Model
- **Status**: Active
- **Location**: `/root/queen-model/`
- **Permissions**: Full Access (Read/Write/Execute)
- **Confirmation Required**: Only for modifications/deletions

## Secondary Agents
- **Hybrid Agent**: `/root/hybrid_agent_project/`
- **Local Models**: `/root/local/`

### Permission Levels

#### Queen Model (Primary)
- ✅ All port access
- ✅ All command execution
- ✅ File read/write
- ✅ System operations
- ⚠️ Confirmation needed for: Deletions, Modifications, Configuration changes

#### Other Models (Secondary)
- ✅ Read operations
- ✅ Non-destructive commands
- ⚠️ Confirmation needed for: Deletions, Modifications, Destructive operations

## VPS Information
- **OS**: Ubuntu Linux
- **Python Version**: 3.12
- **GPU**: NVIDIA CUDA 13
- **Available Models**:
  - Queen Model (Hugging Face)
  - Hybrid Agent Project
  - Local Models (2-part safetensors)

## Safety Protocol
1. All commands logged
2. Confirmation prompts for critical operations
3. Model-based permission hierarchy
4. Audit trail maintained

**Last Updated**: 2026-05-23