# Codex Skills Quickstart

Bu projede Codex skill paketleri `.agents/skills` altında tutulur.

## Skills nasıl çağrılır?
- Explicit çağrı: prompt içinde `$skill-name` kullan.
- Örnekler:
  - `$plan-writing ile bu feature için görev planı çıkar.`
  - `$workflow-debug çalıştır ve hatanın kök nedenini bul.`
  - `$role-backend-specialist olarak API katmanını iyileştir.`

## Role örnekleri
- `role-backend-specialist olarak davran; mevcut endpointleri güvenli ve performanslı hale getir.`
- `role-frontend-specialist olarak davran; erişilebilir ve responsive bir UI revizyonu yap.`
- `role-security-auditor olarak davran; savunmacı güvenlik bulguları ve düzeltme planı çıkar.`

## 8 hazır deneme promptu
1. **API**: `$role-backend-specialist ve $api-patterns kullanarak yeni /v2/orders endpointini tasarla; testlerini ekle.`
2. **UI**: `$role-frontend-specialist ve $frontend-design ile checkout sayfasını erişilebilirlik odaklı yenile.`
3. **DB migration**: `$role-database-architect ile users tablosuna soft-delete migration planı oluştur ve backward compatibility kontrolü yap.`
4. **CI/CD**: `$role-devops-engineer ve $workflow-deploy ile staging deploy pipeline'ını güvenli varsayılanlarla güncelle.`
5. **Debug**: `$workflow-debug + $role-debugger ile login sırasında oluşan 500 hatasını kök neden analiziyle çöz.`
6. **Perf**: `$workflow-perf ve $role-performance-optimizer ile ilk yüklenme süresini azaltacak en etkili 3 iyileştirmeyi uygula.`
7. **Security audit**: `$workflow-security ve $role-security-auditor ile savunmacı güvenlik denetimi yap; exploit üretmeden bulguları sırala.`
8. **Docs**: `$workflow-doc ve $role-documentation-writer ile API kullanım rehberini örnek istek/yanıtlarla güncelle.`
