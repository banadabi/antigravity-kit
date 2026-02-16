# AGENTS.md

## Working agreement
- Önce hızlı keşif yap: `rg`, `find`, dosya listesi ve ilgili modül yollarını belirle.
- Sonra hedef odaklı okuma yap: yalnızca değişecek dosyaları ve bağımlı kritik dosyaları aç (selective reading).
- Büyük kod tabanlarında gereksiz tam tarama yerine dar kapsamlı arama tercih et.

## Modern engineering defaults
- Güvenli varsayılanlarla ilerle: en az yetki, güvenli config, açık hata mesajları yerine kontrollü loglama.
- Dependency güncellemelerinde resmi doküman/changelog önceliklidir.
- Riskli veya mimari etkisi yüksek değişikliklerde küçük, geri alınabilir PR dilimlerine böl.

## Skill policy
- Uygunsa skill çağrısını explicit yap: `$skill-name`.
- Görev tanımı bir skill description ile güçlü eşleşiyorsa implicit skill seçimine izin ver.
- Birden çok skill gerektiğinde en az set ile başla, ihtiyaç oldukça genişlet.

## Plan & execution
- Önce kısa plan çıkar (3-6 adım).
- Sonra küçük artımlı değişiklikler yap.
- Ardından ilgili test/lint/build doğrulamalarını çalıştır.
- En sonda yapılanları ve doğrulama çıktısını kısa bir özetle paylaş.

## Security policy
- Secret, token, private key veya hassas kimlik bilgilerini asla yazdırma/commit etme.
- Red-team / penetration içeriği yalnızca savunma, hardening ve izinli test bağlamında ele alınır.
- Üretime zarar verebilecek, izinsiz erişim veya exploit odaklı yönlendirme verilmez.
