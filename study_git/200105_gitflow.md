# Git Flow
Git Branching Model

수많은 branching 작업을 규격화하여 쉽게 다룰 수 있도록 해 주는 규칙!

---

## 기본 branch models
**feature**
- 새로운 기능 추가용 (origin에 업로드X)
- 특정 기능에 대한 개발 필요시, develop branch에서 파생됨. 개발 완료 후 다시 develop branch로 병합.

**develop & master**
- 중심이 되는, 무조건 존재해야 하는 branch.
- develop에서 개발된 프로젝트는 release를 통해 준비, master로 병합됨.

**release**
- 지금까지 개발한 기능들을 develop branch에서 따내 release branch를 만들고, 여기서 발견되는 버그들을 수정하며  release 준비.
- 그동안 develop branch에서는 다음 release를 위한 준비.
- release 준비 완료 시, master에 병합. 이 때, release에서 수정된 버그는 develop에도 병합하여 적용시킴.

**hotfix**
- release 이후 발생한 버그 수정용
- master branch로부터 파생됨.
- 수정된 버그는 master, develop에 모두 병합. (release 존재 시, 또한 병합)