class DocumentIngestorAgent:
    def ingest(self, file_path):
        """문서 파일을 입력받아 텍스트로 변환/전처리"""
        pass

class SectionClassifierAgent:
    def classify(self, text):
        """문서 텍스트를 섹션별로 분리"""
        pass

class QAAssistantAgent:
    def answer(self, question, sections):
        """질문에 대해 섹션 기반 답변 생성"""
        pass

class ComplianceDetectorAgent:
    def detect(self, sections):
        """컴플라이언스 이슈 자동 탐지"""
        pass

class EscalationAgent:
    def escalate(self, issue):
        """복잡/자동화 불가 이슈를 담당자에게 에스컬레이션"""
        pass

class TicketGeneratorAgent:
    def generate(self, issue):
        """이슈/질문에 대해 티켓(이슈/작업) 자동 생성"""
        pass 